import React, {useState} from 'react'
import { Link } from 'react-router-dom'


function Navbar() {
  const [click, setClick] = useState(false);

  const handleClick = () => setClick(!click);

  const closeMobileMenue = () => setClick(false);

  return (
    <>
        <nav className='navbar'>
            <div className='navbar-container'>
                <Link to='/' className='navbar-logo'> 
                  insert icon here <i className='fab fa-typo3' />
                </Link>
                <div className='menue-icon' onClick={handleClick}>
                  <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                </div>
                <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                  <li className='nav-item'>
                    <Link to='/' className='nav-links' onClick={closeMobileMenue}>
                      Home
                    </Link>
                  </li>
                  <li className='nav-item'>
                    <Link to='/services' className='nav-links' onClick={closeMobileMenue}>
                      Services
                    </Link>
                  </li>
                  <li className='nav-item'>
                    <Link to='/products' className='nav-links' onClick={closeMobileMenue}>
                      Products
                    </Link>
                  </li>
                  <li className='nav-item'>
                    <Link to='/signup' className='nav-links' onClick={closeMobileMenue}>
                      Signup
                    </Link>
                  </li>
                </ul>
            </div>
        </nav>
    </>
  )
}

export default Navbar