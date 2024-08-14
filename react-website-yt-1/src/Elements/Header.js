import React from 'react'
import './header.css'
export const Header = () => {
  return (
   <header className="header">
      <img src={`${process.env.PUBLIC_URL}/Logo-Soccer.png`} alt="Logo" className="navbar-logo" />

      <nav className="navbar">
        <a href="/">Control</a>
        <a href="/">Offense</a>
        <a href="/">Defense</a>
        <a href="/">Services</a>
        <a href="/">Contact</a>




      </nav>
   </header>
  )

}
