import React, { useEffect, useRef } from 'react';
import './Hero.css';

export const Hero = () => {
  const heroRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          heroRef.current.classList.add('fade-in');
          heroRef.current.classList.remove('fade-out');
        } else {
          heroRef.current.classList.add('fade-out');
          heroRef.current.classList.remove('fade-in');
        }
      },
      {
        threshold: 0.5, 
      }
    );

    if (heroRef.current) {
      observer.observe(heroRef.current);
    }

    return () => {
      if (heroRef.current) {
        observer.unobserve(heroRef.current);
      }
    };
  }, []);

  return (
    <section className="hero" ref={heroRef}>
      <div className="hero-image">
        <img src={`${process.env.PUBLIC_URL}/Qatar-logo.png`} alt="Hero" />
      </div>
      <div className="hero-text">
        <h1>WorldCupStats</h1>
        <p>This is WorldCupStats' statistical analysis of Qatar's 2022 World Cup. Very Cool.</p>
      </div>
    </section>
  );
};
