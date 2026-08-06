"use client"

import Image from "next/image"
import { useState, useEffect, useRef } from "react"

const ACCESS_PASSWORD = "EASTSE"

export default function Page() {
  const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 })
  const [needsPermission, setNeedsPermission] = useState(false)
  const [gyroActive, setGyroActive] = useState(false)
  const [shouldAnimate, setShouldAnimate] = useState(false)
  const [animationComplete, setAnimationComplete] = useState(false)

  // login state
  const [password, setPassword] = useState("")
  const [error, setError] = useState(false)
  const [shake, setShake] = useState(false)
  const [authenticating, setAuthenticating] = useState(false)
  const [unlocked, setUnlocked] = useState(false)
  const inputRef = useRef<HTMLInputElement>(null)

  const frameRef = useRef<number>()
  const lastUpdateRef = useRef<number>(0)

  const requestOrientation = async () => {
    if (typeof (DeviceOrientationEvent as any).requestPermission === "function") {
      try {
        const permissionState = await (DeviceOrientationEvent as any).requestPermission()
        if (permissionState === "granted") {
          setNeedsPermission(false)
          setGyroActive(true)
          setShouldAnimate(true)
        }
      } catch (error) {
        console.error("Permission denied:", error)
      }
    } else {
      setNeedsPermission(false)
      setGyroActive(true)
      setShouldAnimate(true)
    }
  }

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const x = (e.clientX - window.innerWidth / 2) / window.innerWidth
      const y = (e.clientY - window.innerHeight / 2) / window.innerHeight
      setMousePosition({ x, y })
    }

    const handleOrientation = (e: DeviceOrientationEvent) => {
      const now = Date.now()
      if (now - lastUpdateRef.current < 16) {
        return
      }
      lastUpdateRef.current = now

      if (frameRef.current) {
        cancelAnimationFrame(frameRef.current)
      }

      frameRef.current = requestAnimationFrame(() => {
        const isLandscape = window.innerWidth > window.innerHeight

        let x = 0
        if (isLandscape) {
          const beta = e.beta || 0
          x = Math.max(-1, Math.min(1, beta / 45))
        } else {
          const gamma = e.gamma || 0
          x = Math.max(-1, Math.min(1, gamma / 45))
        }
        const y = 0

        setMousePosition({ x, y })
      })
    }

    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent)
    const isTablet = /iPad|Android/i.test(navigator.userAgent) && window.innerWidth >= 768
    const isTouchDevice = isMobile || isTablet || "ontouchstart" in window || navigator.maxTouchPoints > 0

    if (isTouchDevice) {
      if (typeof (DeviceOrientationEvent as any).requestPermission === "function") {
        setNeedsPermission(true)
      } else {
        setGyroActive(true)
        setShouldAnimate(true)
      }
    } else {
      window.addEventListener("mousemove", handleMouseMove)
      setShouldAnimate(true)
    }

    if (gyroActive) {
      window.addEventListener("deviceorientation", handleOrientation)
    }

    return () => {
      window.removeEventListener("mousemove", handleMouseMove)
      window.removeEventListener("deviceorientation", handleOrientation)
      if (frameRef.current) {
        cancelAnimationFrame(frameRef.current)
      }
    }
  }, [gyroActive])

  useEffect(() => {
    const timer = setTimeout(() => {
      setAnimationComplete(true)
    }, 4000)
    return () => clearTimeout(timer)
  }, [])

  // focus input once the entrance animation settles
  useEffect(() => {
    if (animationComplete && inputRef.current) {
      inputRef.current.focus()
    }
  }, [animationComplete])

  // redirect after unlock
  useEffect(() => {
    if (unlocked) {
      const t = setTimeout(() => {
        window.location.href = "/index.html"
      }, 900)
      return () => clearTimeout(t)
    }
  }, [unlocked])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (authenticating || unlocked) return
    setAuthenticating(true)
    setError(false)
    setTimeout(() => {
      if (password.trim().toUpperCase() === ACCESS_PASSWORD) {
        try {
          sessionStorage.setItem("lisa-auth", "1")
        } catch (_) {}
        setUnlocked(true)
      } else {
        setError(true)
        setShake(true)
        setPassword("")
        setTimeout(() => setShake(false), 500)
      }
      setAuthenticating(false)
    }, 350)
  }

  return (
    <div className="relative h-dvh w-full overflow-hidden bg-black">
      {needsPermission && (
        <div className="absolute inset-0 z-50 flex items-center justify-center bg-black/80">
          <button
            onClick={requestOrientation}
            className="px-8 py-4 bg-orange-600 text-white text-xl font-bold rounded-lg hover:bg-orange-700 transition-colors"
          >
            Enable Parallax Effect
          </button>
        </div>
      )}

      <div
        className={`absolute inset-0 ${shouldAnimate ? "zoom-layer-1" : ""}`}
        style={{
          transform: `translate3d(${mousePosition.x * 30}px, ${mousePosition.y * 30}px, 0)`,
          willChange: "transform",
          width: "130%",
          height: "130%",
          left: "-15%",
          top: "-15%",
        }}
      >
        <Image src="/images/earth-1.jpg" alt="Earth from space" fill className="object-cover" priority />
      </div>

      <div
        className={`absolute z-5 ${shouldAnimate ? "zoom-layer-starship" : ""}`}
        style={{
          transform: `translate3d(${mousePosition.x * 50}px, ${mousePosition.y * 50}px, 0) scale(0.75)`,
          willChange: "transform",
          width: "800px",
          height: "800px",
          left: "20px",
          top: "20px",
        }}
      >
        <Image src="/images/starship_lenovo_complete_object.png" alt="Space station" fill className="object-contain" />
      </div>

      <div
        className={`absolute inset-0 z-10 ${shouldAnimate ? "zoom-layer-2" : ""}`}
        style={{
          transform: `translate3d(${mousePosition.x * 60}px, ${mousePosition.y * 60}px, 0)`,
          willChange: "transform",
          width: "130%",
          height: "130%",
          left: "-15%",
          top: "-15%",
        }}
      >
        <Image src="/images/mars-2.png" alt="Spacecraft interior window" fill className="object-cover" />
      </div>

      <div
        className={`absolute inset-0 flex items-center justify-center z-10 px-6 ${shouldAnimate ? "zoom-layer-text" : ""} ${unlocked ? "unlocked-rise" : ""}`}
        style={{
          transform: `translate3d(${mousePosition.x * 90}px, ${mousePosition.y * 90}px, 0)`,
          willChange: "transform",
          perspective: "1000px",
        }}
      >
        <div className="flex flex-col items-center">
          <div className="flex text-[80px] sm:text-[120px] md:text-[160px] lg:text-[200px] leading-none">
            {"LISA".split("").map((letter, index) => (
              <span
                key={index}
                className={`font-bold text-white ${shouldAnimate ? "letter-rotate" : ""}`}
                style={{
                  display: "inline-block",
                  transformStyle: "preserve-3d",
                  animationDelay: `${index * 0.12}s`,
                }}
              >
                {letter}
              </span>
            ))}
          </div>
          <div
            className={`mt-4 text-center ${shouldAnimate ? "fade-in-sub" : ""}`}
            style={{ opacity: 0 }}
          >
            <p className="text-white/60 text-sm sm:text-base tracking-[0.35em] uppercase font-light">
              Lenovo Intelligent Storage Agent
            </p>
          </div>
        </div>
      </div>

      <div
        className={`absolute inset-0 z-20 ${shouldAnimate ? "zoom-layer-3" : ""} ${unlocked ? "unlocked-fade" : ""}`}
        style={{
          transform: `translate3d(${mousePosition.x * 120}px, ${mousePosition.y * 120}px, 0)`,
          willChange: "transform",
          width: "110%",
          height: "110%",
          left: "-5%",
          top: "calc(-5% + 150px)",
        }}
      >
        <Image src="/images/mars-3.png" alt="Astronaut in orange spacesuit" fill className="object-cover" />
      </div>

      {/* ===== Access login overlay ===== */}
      <div
        className={`absolute inset-0 z-40 flex items-center justify-center px-6 transition-all duration-700 ${
          animationComplete ? "opacity-100" : "opacity-0 pointer-events-none"
        } ${unlocked ? "opacity-0" : ""}`}
      >
        <div
          className={`absolute inset-0 bg-black/30 backdrop-blur-[2px] transition-opacity duration-700 ${
            unlocked ? "opacity-0" : "opacity-100"
          }`}
        />
        <form
          onSubmit={handleSubmit}
          className={`relative w-full max-w-sm ${shake ? "shake-anim" : ""}`}
        >
          <div className="relative rounded-2xl border border-white/15 bg-white/[0.06] px-8 py-9 shadow-[0_20px_80px_-20px_rgba(0,0,0,0.8)] backdrop-blur-xl">
            <div className="mb-6 text-center">
              <div className="mx-auto mb-4 flex h-10 w-10 items-center justify-center rounded-full border border-white/20 bg-white/5">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-white/80">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                </svg>
              </div>
              <h1 className="text-white text-lg font-semibold tracking-wide">Access Required</h1>
              <p className="text-white/50 text-xs mt-1.5 tracking-wider">Enter access code to continue</p>
            </div>

            <div className="relative">
              <input
                ref={inputRef}
                type="password"
                value={password}
                onChange={(e) => {
                  setPassword(e.target.value)
                  if (error) setError(false)
                }}
                placeholder="••••••"
                autoComplete="off"
                spellCheck={false}
                className={`w-full rounded-xl border bg-black/30 px-4 py-3.5 text-center text-white text-lg tracking-[0.4em] placeholder:text-white/25 outline-none transition-all duration-200 ${
                  error
                    ? "border-red-400/60 focus:border-red-400"
                    : "border-white/15 focus:border-cyan-300/60 focus:bg-black/40"
                }`}
              />
            </div>

            {error && (
              <p className="mt-3 text-center text-red-400 text-xs tracking-wide">
                Incorrect access code. Please try again.
              </p>
            )}

            <button
              type="submit"
              disabled={authenticating || unlocked}
              className="mt-5 w-full rounded-xl bg-gradient-to-r from-cyan-400/90 to-blue-500/90 px-4 py-3.5 text-sm font-semibold text-black tracking-wider transition-all duration-200 hover:from-cyan-300 hover:to-blue-400 hover:shadow-[0_0_30px_-5px_rgba(56,189,248,0.6)] active:scale-[0.98] disabled:opacity-50"
            >
              {unlocked ? "Access Granted" : authenticating ? "Verifying…" : "Enter"}
            </button>

            <p className="mt-5 text-center text-white/30 text-[10px] tracking-[0.3em] uppercase">
              LiSA · Confidential
            </p>
          </div>
        </form>
      </div>

      {/* Unlocking overlay flash */}
      <div
        className={`absolute inset-0 z-50 bg-white transition-opacity duration-700 ${
          unlocked ? "opacity-80" : "opacity-0 pointer-events-none"
        }`}
      />

      <style jsx>{`
        .zoom-layer-1 {
          animation: zoomOut1 8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        .zoom-layer-starship {
          animation: zoomOutStarship 8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        .zoom-layer-2 {
          animation: zoomOut2 8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        .zoom-layer-3 {
          animation: zoomOut3 8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        .zoom-layer-text {
          animation: zoomOutText 8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        .fade-in-sub {
          animation: fadeInSub 1.5s 5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        .unlocked-rise {
          animation: unlockedRise 0.9s cubic-bezier(0.4, 0, 0.2, 1) forwards !important;
        }
        .unlocked-fade {
          animation: unlockedFade 0.9s cubic-bezier(0.4, 0, 0.2, 1) forwards !important;
        }
        .shake-anim {
          animation: shake 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
        }

        @keyframes zoomOut1 {
          0% { scale: 1.3; }
          100% { scale: 1; }
        }

        @keyframes zoomOutStarship {
          0% { scale: 1.5; }
          100% { scale: 0.75; }
        }

        @keyframes zoomOut2 {
          0% { scale: 2.5; filter: blur(20px); }
          50% { filter: blur(10px); }
          100% { scale: 1; filter: blur(0px); }
        }

        @keyframes zoomOut3 {
          0% { scale: 8; filter: blur(40px); opacity: 0; }
          30% { filter: blur(25px); opacity: 0.3; }
          70% { filter: blur(10px); opacity: 0.7; }
          100% { scale: 1; filter: blur(0px); opacity: 1; }
        }

        @keyframes zoomOutText {
          0% { scale: 3.5; opacity: 0; }
          40% { opacity: 0.3; }
          70% { opacity: 0.7; }
          100% { scale: 1; opacity: 1; }
        }

        @keyframes fadeInSub {
          0% { opacity: 0; transform: translateY(10px); }
          100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes unlockedRise {
          0% { opacity: 1; }
          100% { opacity: 0; transform: translateY(-60px); }
        }

        @keyframes unlockedFade {
          0% { opacity: 1; }
          100% { opacity: 0; }
        }

        .letter-rotate {
          animation: rotateText 8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }

        @keyframes rotateText {
          0% { transform: rotateY(90deg); filter: blur(30px); opacity: 0; }
          40% { filter: blur(15px); opacity: 0.5; }
          70% { filter: blur(5px); opacity: 0.8; }
          100% { transform: rotateY(0deg); filter: blur(0px); opacity: 1; }
        }

        @keyframes shake {
          10%, 90% { transform: translateX(-1px); }
          20%, 80% { transform: translateX(2px); }
          30%, 50%, 70% { transform: translateX(-4px); }
          40%, 60% { transform: translateX(4px); }
        }
      `}</style>
    </div>
  )
}
