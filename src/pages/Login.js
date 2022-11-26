import React, { useState } from "react";
import {useNavigate} from 'react-router-dom';
import bcrypt from 'bcryptjs'
import './AuthForm.css';

export default function Login({setLoginStatus}){
    const navigate = useNavigate();
    const [uname, setUname] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        ApiLogin();
    }

    function ApiLogin(){
        const hashedPass = bcrypt.hashSync(pass, '$2a$10$ovfJgA/SxVxsd3NeD3dMne') //If u change the salt also change it in CreateUser.js
        fetch(`http://localhost:8000/login?username=${uname}&password=${hashedPass}`).then(res => res.json()).then(data => {
            if(data.login){
                setLoginStatus(uname, data.isAdmin, data.userToken);
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

