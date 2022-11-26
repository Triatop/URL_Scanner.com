import './App.css';
import Navbar from './components/Navbar';
import SearchbarContainer from './components/SearchbarContainer';

import History from './pages/History';
import Login from './pages/Login';
import Logout from './pages/Logout';
import UserHistory from './pages/UserHistory';
import CreateUser from './pages/CreateUser';
import {BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom';
import {useState, useEffect} from "react";
import {DarkModeToggle} from '@anatoliygatt/dark-mode-toggle';



function App() {
  
  const [mode, setMode] = useState("dark");           //Darkmode - Lightmode
  const [user, setUser] = useState('');               //Not empty if the user is logged in
  const [admin, setAdmin] = useState(false);          //True if the the logged in user is an Admin
  const [userToken, setUserToken] = useState(''); //Session token connected to the user

  const setLoginStatus = (username,isAdmin, token) => { //passed into Login and Logout to get info about the user
    setUser(username);
    setAdmin(isAdmin);
    setUserToken(token);
  }

  useEffect(() => {
    const data = window.localStorage.getItem('userToken');  //get admin when window is refreshed
    if ( data !== null ) setUserToken(JSON.parse(data));
  }, []);

  useEffect(()=>{
    window.localStorage.setItem('userToken', JSON.stringify(userToken)) //store admin when windows is refreshed
  },[userToken]);

  useEffect(() => {
    const data = window.localStorage.getItem('admin');  //get admin when window is refreshed
    if ( data !== null ) setAdmin(JSON.parse(data));
  }, []);

  useEffect(()=>{
    window.localStorage.setItem('admin', JSON.stringify(admin)) //store admin when windows is refreshed
  },[admin]);

  useEffect(() => {
    const data = window.localStorage.getItem('user'); //get user when window is refreshed
    if ( data !== null ) setUser(JSON.parse(data));
  }, []);

  useEffect(()=>{
    window.localStorage.setItem('user', JSON.stringify(user)) //store user when window is refreshed
  },[user]);

  useEffect(() => {
    const data = window.localStorage.getItem('darkmode'); //get mode when window is refreshed
    if ( data !== null ) setMode(JSON.parse(data));
  }, []);

  useEffect(()=>{
    window.localStorage.setItem('darkmode', JSON.stringify(mode)) //store mode when window is refreshed
  },[mode]);

  const ProtectedRouteUser = ({ children }) => { //protect routes from unregisterd users
    if (user === '') {
      return <Navigate to="/" replace />;
    }
    return children;
  };

  const ProtectedRouteAdmin = ({ children }) => { //protect routes from non admin users
    if (!admin) {
      return <Navigate to="/" replace />;
    }
    return children;
  };

  return (
      <div className='App' id={mode}>
      <Router>
      <div className='topRow'>
        <Navbar user={user} admin={admin}/>
        <div className="switch">
              <DarkModeToggle 
              checked={mode === "dark"} 
              mode={mode}
              onChange={(mode) => {
                setMode(mode);
              }}/>
        </div>
      </div>
      <div className='container'>
        <Routes>
          <Route path='/' element={<SearchbarContainer/>} />
          <Route path='/login' element={<Login setLoginStatus={setLoginStatus}/>} />
          <Route path='/logout' element={<Logout setLoginStatus={setLoginStatus}/>} />
          <Route path='/createuser' element={<ProtectedRouteAdmin > <CreateUser user={user} userToken={userToken}/> </ProtectedRouteAdmin> } /> 
          <Route path='/history' element={<ProtectedRouteUser > <History user={user} userToken={userToken}/> </ProtectedRouteUser> } />
          <Route path='/userhistory' element={<ProtectedRouteAdmin > <UserHistory user={user} userToken={userToken}/> </ProtectedRouteAdmin>} />
          <Route path='*' element={<Navigate to='/' replace/>} />
        </Routes>
      </div>
      </Router>
      </div>
  );
}

export default App;
