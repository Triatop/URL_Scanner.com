import React, {useState, useEffect} from 'react'
//import { Link } from 'react-router-dom'
import './Searchbar.css';

//this shit right here!!:
//https://stackoverflow.com/questions/72343715/sending-form-data-from-frontend-to-backend-using-axios-using-react

function Searchbar(){

  const [inputValue, setInputValue] = useState('');
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
      if (event.key === 'Enter'){
          event.preventDefault();
          StartScanner();
          
      }
  }

  function StartScanner(){
    fetch(`/backendAPI?url=${inputValue}`).then(res => res.json()).then(data => {
      setReturnDict(data)
    });

    setShow(true)
  }

  return (
    <div className='Searchbar'>
        <input
          type="text"
          class="search"
          name="inputValue"
          onChange={handleChange}
          value={inputValue}
          autoComplete="off"
          placeholder='Place/type ULR here...'
          onKeyDown={keyDwonHandeler}
        />
      <div className='Searchbtn'>
          <button type='button'onClick={handleClick} >SCAN</button>
      </div>
      {
      show?<div>
        <section id="report">
          <p>Valid URL: {returnDict.valid}</p>
          <p>{returnDict.report}</p>
        </section>
      </div>:null
      }
    </div>
  );

}

export default Searchbar;