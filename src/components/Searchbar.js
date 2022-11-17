import React, { useState, useEffect } from 'react'
//import { Link } from 'react-router-dom'
import './Searchbar.css';
import LoadingSpinner from './LoadingSpinner'

//this shit right here!!:
//https://stackoverflow.com/questions/72343715/sending-form-data-from-frontend-to-backend-using-axios-using-react

//Arvid was here.

function Searchbar() {

  const [inputValue, setInputValue] = useState('');
  const [isLoading, setLoading] = useState(false)
  // const [currentTime, setCurrentTime] = useState(0);
  const [returnDict, setReturnDict] = useState('');
  const [show, setShow] = useState(false);




  const handleChange = event => {
    if (event.key !== 'Enter')
      setInputValue(event.target.value);
  };

  const handleClick = event => {
    event.preventDefault();
    StartScanner();
  };

  const keyDwonHandeler = event => {
    if (event.key === 'Enter') {
      event.preventDefault();
      StartScanner();

    }
  }

  function StartScanner() {
    setLoading(true)
    setReturnDict('')
    fetch(`http://localhost:8000/backendAPI?url=${inputValue}`).then(res => res.json()).then(data => {
      setReturnDict(data)
      setLoading(false)
      setShow(true)
    });
  }

  return (
    <div className='SearchbarContainer'>
      <div className="Searchbar">
        <input
          type="text"
          class="search"
          name="inputValue"
          onChange={handleChange}
          value={inputValue}
          autoComplete="off"
          placeholder='Place/type URL here...'
          onKeyDown={keyDwonHandeler}
        />
        <div className="LoadingSpinner">
          {isLoading ? <LoadingSpinner></LoadingSpinner> : ''}
        </div>
      </div>
      <div className='Searchbtn'>
        <button type='button' onClick={handleClick} >SCAN</button>
      </div>
      {
        show ? <div>
          <section className="report">
            <p>Valid URL: {returnDict.valid} {returnDict.reDirect}</p>
            <p>{returnDict.report} {returnDict.exeTime} {returnDict.binarySafe}</p>
          </section>
        </div> : null
      }
    </div>
  );

}

export default Searchbar;