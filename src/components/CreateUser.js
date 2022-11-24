import React, { useState } from "react";
import bcrypt from 'bcryptjs'
import './AuthForm.css';

export const CreateUser = (props) => {
    const [uname, setUname] = useState('');
    const [pass, setPass] = useState('');
    const [name, setName] = useState('');
    const [showResp, setShowResp] = useState()

    const handleSubmit = (e) => {
        e.preventDefault();
        ApiCreateUser()
    }

    function ApiCreateUser(){
        const hashedPass = bcrypt.hashSync(pass, '$2a$10$ovfJgA/SxVxsd3NeD3dMne') //If u change the salt also change it in Login.js
        setShowResp(false)
        fetch(`http://localhost:8000/createuser?username=${uname}&password=${hashedPass}&fullname=${name}`).then(res => res.json()).then(data => {
            if(data.creation){
                setShowResp(true)
            }
        });
    }

    return (
        <div>
            <div className="auth-form-container">
                <h2>Create User</h2>
            <form className="create-user-form" onSubmit={handleSubmit}>
                <label htmlFor="name">Full Name</label>
                <input value={name} onChange={(e) => setName(e.target.value)} type="name" placeholder="name" id="name" name="name"  />
                <label htmlFor="uname">Username </label>
                <input value={uname} onChange={(e) => setUname(e.target.value)} type="username" placeholder="username" id="uname" name="uname" />
                <label htmlFor="password">Password</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                <button type="submit">Create</button>
            </form>
            </div>
            {showResp ? <h3>Create a string here that says if it was successfull or not</h3>: null}
        </div>
    )
}