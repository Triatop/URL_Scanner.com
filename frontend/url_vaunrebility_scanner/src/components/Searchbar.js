import React, {useState, useEffect} from 'react'
//import { Link } from 'react-router-dom'
import './Searchbar.css';

//this shit right here!!:
//https://stackoverflow.com/questions/72343715/sending-form-data-from-frontend-to-backend-using-axios-using-react

function Searchbar(){

  const [inputValue, setInputValue] = useState('');
  const [currentTime, setCurrentTime] = useState(0);
  const [returnDict, setReturnDict] = useState('');
 

  useEffect(() => {
    fetch(`/backendAPI?url=${inputValue}`).then(res => res.json()).then(data => {
      setCurrentTime(data);
    });
  }, []);

  useEffect(() => {
    fetch('/scanner').then(res => res.json()).then(data => {
      setReturnDict(data.report);
    });
  }, []);

  const handleChange = event => {
      if (event.key !== 'Enter')
      setInputValue(event.target.value);
  };

  const handleClick = event => {
      event.preventDefault();
      StartScanner();
  };
  
  const keyDwonHandeler = event => {
      if (event.key === 'Enter'){
          event.preventDefault();
          StartScanner();
      }
  }

  function StartScanner(){
    /*api call*/
    console.log("ULR:", inputValue);
    console.log(returnDict)
  }

  return (
    <div className='Searchbar'>
      <input
        type="text"
        id="inputValue"
        name="inputValue"
        onChange={handleChange}
        value={inputValue}
        autoComplete="off"
        placeholder='Place/type ULR here...'
        onKeyDown={keyDwonHandeler}
      />
      <div className='Searchbtn'>
          <button type='button' onClick={handleClick}>Scan</button>
      </div>
      <div>
        <p>The current time is {currentTime}.</p>
        <p>Report: {returnDict}</p>
      </div>
    </div>
  );

}

export default Searchbar;