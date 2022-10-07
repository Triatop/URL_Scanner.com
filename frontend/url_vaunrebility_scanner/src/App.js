import './App.css';
import Navbar from './components/Navbar';
import Searchbar from './components/Searchbar';
import LoginBtn from './components/LoginBtn';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <div className='App'>
    <Router>
     {/*<Navbar />*/}
     <LoginBtn/>
     <Searchbar />
      <Routes>
        <Route path='/' exact />
      </Routes>
    </Router>
    </div>
  );
}

export default App;
