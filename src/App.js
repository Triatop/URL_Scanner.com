import './App.css';
// import Navbar from './components/Navbar';
import SearchbarContainer from './components/SearchbarContainer';
import LoginBtn from './components/LoginBtn';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import {useState} from "react";
import {DarkModeToggle} from '@anatoliygatt/dark-mode-toggle';



function App() {
  
  const [mode, setMode] = useState("dark");

  return (
      <div className='App' id={mode}>
      <Router>
      {/*<Navbar />*/}
      <div className='topRow'>
        <LoginBtn/>
        <div className="switch">
              <DarkModeToggle 
              checked={mode === "dark"} 
              mode={mode}
              onChange={(mode) => {
                setMode(mode);
              }}/>
        </div>
      </div>
      <SearchbarContainer/>
        <Routes>
          <Route path='/' exact />
        </Routes>
      </Router>
      </div>
  );
}

export default App;
