import React, { useState, useEffect } from "react";
import {useNavigate} from 'react-router-dom';
import bcrypt from 'bcryptjs'
import './AuthForm.css';

export default function Login({setLoginStatus}){
    const navigate = useNavigate();
    const [uname, setUname] = useState('');
    const [pass, setPass] = useState('');
    const [response, setResponse] = useState('')
    const [showResp, setShowResp] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault();
        ApiLogin();
    }

    function ApiLogin(){
        setShowResp(false)
        const hashedPass = bcrypt.hashSync(pass, '$2a$10$ovfJgA/SxVxsd3NeD3dMne') //If u change the salt also change it in CreateUser.js
        fetch(`http://localhost:8000/login?username=${uname}&password=${hashedPass}`).then(res => res.json()).then(data => {
            if(data.login){
                setLoginStatus(uname, data.isAdmin, data.userToken);
                navigate('/');
            }else{
                setResponse('Invalid login credentials')
                setShowResp(true)
            }
        });
    }

    useEffect(() => {
        window.scrollTo(0, 0)
    }, [])

    return (
        <div>
            <div className="auth-form-container">
                <h2>Login</h2>
                <form className="login-form" onSubmit={handleSubmit}>
                    <label htmlFor="uname">Username</label>
                    <input className="inputFields" value={uname} onChange={(e) => setUname(e.target.value)}type="username" placeholder="username" id="uname" name="uname" />
                    <label htmlFor="password">Password</label>
                    <input className="inputFields" value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                    <div className="AuthBtnContainer">
                        <button className="loginBtn" type="submit">Log In</button>
                    </div>
                </form>
            </div>
            <div>
                {showResp ? <p>{response}</p> : null}
            </div>
        </div>
    )
}

