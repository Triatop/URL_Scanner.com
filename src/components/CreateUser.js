import React, { useState } from "react";
import './AuthForm.css';

export const CreateUser = (props) => {
    const [uname, setUname] = useState('');
    const [pass, setPass] = useState('');
    const [name, setName] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(uname, pass, name);
    }

    //Do api call
    
    //Create a function that tells the admin if the user creation was successfull or not

    return (
        <div className="auth-form-container">
            <h2>Create User</h2>
        <form className="create-user-form" onSubmit={handleSubmit}>
            <label htmlFor="name">Full Name</label>
            <input value={name} onChange={(e) => setName(e.target.value)} name="name" id="name" placeholder="name" />
            <label htmlFor="uname">Username </label>
            <input value={uname} onChange={(e) => setUname(e.target.value)} type="username" placeholder="username" id="uname" name="uname" />
            <label htmlFor="password">Password</label>
            <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
            <button type="submit">Create</button>
        </form>
    </div>
    )
}