import React, { useState } from "react";
import {useNavigate} from 'react-router-dom';
import './AuthForm.css';

export default function Login({setLoginStatus}){
    const navigate = useNavigate();
    const [uname, setUname] = useState('');
    const [pass, setPass] = useState('');
    const [isAdmin, setIsAdmin] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault();
        setLoginStatus('Hugin',true)
        navigate('/');
    }

    //Do api call

    //Create functions here that tells the user if the loggin was success full or not

    //If the login is successfull - redirect the user to the home page

    return (
        <div className="auth-form-container">
            <h2>Login</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="uname">Username</label>
                <input value={uname} onChange={(e) => setUname(e.target.value)}type="username" placeholder="username" id="uname" name="uname" />
                <label htmlFor="password">Password</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                <button type="submit">Log In</button>
            </form>
        </div>
    )
}

