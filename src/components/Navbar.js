import { Link, useMatch, useResolvedPath } from "react-router-dom"
import {useState, useEffect} from "react";
import "./Navbar.css"

export default function Navbar({user, admin}) {
  const [showUser, setShowUser] = useState(true)
  const [showAdmin, setShowAdmin] = useState(false)

  useEffect(() => {
    if(user.length !== 0){
      setShowUser(true)
    }else{
      setShowUser(false)
    }

    if(admin){
      setShowAdmin(true)
    }else{
      setShowAdmin(false)}
  })
  
  return (
    <div className="toprowchild">
      <nav className="nav">
        <Link to="/" className="site-title">
          URL SCANNER
        </Link>
        <ul>
          <CustomLink to="/">Home</CustomLink>
          { !showUser ? <CustomLink to="/login">Login</CustomLink>: null}
          { showAdmin ? <CustomLink to="/createuser">Create User</CustomLink>: null}
          { showUser ? <CustomLink to="/history">History</CustomLink>: null}
          { showAdmin ? <CustomLink to="/userhistory">User History</CustomLink>: null}
          { showUser ? <CustomLink to="/logout">Logout</CustomLink>: null}
        </ul>
      </nav>
      <div className="welcome">
        { showUser ? <p> Welcome: {user}</p>: null}
      </div>
    </div>
  )
}

function CustomLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true })

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  )
}