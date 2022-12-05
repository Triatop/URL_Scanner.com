import {useNavigate} from 'react-router-dom';
import {useEffect} from 'react';

import "./Logout.css"

export default function Logout({setLoginStatus}) {
    const navigate = useNavigate();

    const handleClick1 = event =>{
        event.preventDefault()
        setLoginStatus('',false,'')
        navigate('/');
    }

    const handleClick2 = event =>{
        event.preventDefault()
        navigate('/');
    }

    useEffect(() => {
        window.scrollTo(0, 0)
    }, [])

    return (
        <div className='logout'>
            <h2>Are you sure you want to logout?</h2>
            <button className="button" onClick={handleClick1} >Yes</button>
            <button className="button" onClick={handleClick2} >Cancel</button>
        </div>
    );
}