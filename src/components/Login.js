import React, { useState } from "react";
import {useNavigate} from 'react-router-dom';
import './AuthForm.css';

export default function Login({setLoginStatus}){
    const navigate = useNavigate();
    const [uname, setUname] = useState('');
    const [pass, setPass] = useState('');
    // const [isAdmin, setIsAdmin] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault();
        ApiLogin();
    }

    function ApiLogin(){
        fetch(`http://localhost:8000/login?username=${uname}&password=${pass}`).then(res => res.json()).then(data => {
            if(data.login){
                setLoginStatus(uname, data.isAdmin);
                navigate('/');
            }
        });
    }

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

