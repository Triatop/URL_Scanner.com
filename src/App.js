import './App.css';
// import Navbar from './components/Navbar';
import Searchbar from './components/Searchbar';
import LoginBtn from './components/LoginBtn';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import { createContext, useState } from "react";
import { DarkModeToggle } from '@anatoliygatt/dark-mode-toggle';

export const ThemeContext = createContext(null);

function App() {
  const [theme, setTheme] = useState("dark");
  const [mode, setMode] = useState("dark")

  const toggleTheme = () => {
    setTheme((curr) => (curr === "light" ? "dark" : "light"));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      <div className='App' id={theme}>
      <Router>
      {/*<Navbar />*/}
      <div className='topRow'>
        <LoginBtn/>
        <div className="switch">
              <DarkModeToggle 
              checked={theme === "dark"} 
              mode={mode}
              onChange={(mode) => {
                setMode(mode);
                toggleTheme()
              }}/>
            </div>
      </div>
      <Searchbar />
        <Routes>
          <Route path='/' exact />
        </Routes>
      </Router>
      </div>
    </ThemeContext.Provider>
  );
}

export default App;
