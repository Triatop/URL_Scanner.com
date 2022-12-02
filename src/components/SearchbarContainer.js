import React, { useState } from 'react';
import './SearchbarContainer.css';
import './Button.css';
import LoadingSpinner from './LoadingSpinner';
import CheckMark from './CheckMark';
import CrossMark from './CrossMark';

//Arvid was here.

function SearchbarContainer({user}) {
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setLoading] = useState(false);
  const [returnDict, setReturnDict] = useState('');
  const [show, setShow] = useState(false);
  const [isSafe, setIsSafe] = useState(false);
  const [notSafe, setNotSafe] = useState(false);
  const [divMargin, setDivMargin] = useState('large')

  const handleChange = event => {
    if (event.key !== 'Enter')
      setInputValue(event.target.value);
  };

  const handleClick = event => {
    event.preventDefault();
    StartScanner();
  };

  const keyDownHandeler = event => {
    if (event.key === 'Enter') {
      event.preventDefault();
      StartScanner();

    }
  }

  function StartScanner() {
    setDivMargin('large')
    setIsSafe(false)
    setNotSafe(false)
    setShow(false)
    setLoading(true)
    setReturnDict('')
    fetch(`http://localhost:8000/scanner?url=${inputValue}&username=${user}`).then(res => res.json()).then(data => {
      setReturnDict(data)
      setLoading(false)
      setShow(true)
      if (data.binarySafe == null) {
        return
      } else if (data.binarySafe){
        setDivMargin('small')
        setIsSafe(true)
      }else{
        setDivMargin('small')
        setNotSafe(true)
      }
    });
    
  }

  return (
    <div className='SearchbarContainer' id={divMargin}>
      <div className='CheckCrossMark'>
        { isSafe ? <CheckMark/> : null }
        { notSafe ? <CrossMark/> : null }
      </div>
      <div className="Searchbar">
        <input
          type="text"
          className="search"
          name="inputValue"
          onChange={handleChange}
          value={inputValue}
          autoComplete="off"
          placeholder='Place/type URL here...'
          onKeyDown={keyDownHandeler}
        />
        <div className="LoadingSpinner">
          {isLoading ? <LoadingSpinner></LoadingSpinner> : null}
        </div>
      </div>
      <div className='ScanBtn'>
        <button type='button' onClick={handleClick}>SCAN</button>
      </div>
      {
        show ? <div>
          <section className="report">
            <p>{returnDict.reDirect} {returnDict.report} {returnDict.exeTime}</p>
          </section>
        </div> : null
      }
    </div>
  );

}

export default SearchbarContainer;