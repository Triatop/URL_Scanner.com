import React, { useState } from "react";
import bcrypt from 'bcryptjs'
import './AuthForm.css';

export default function CreateUser({user,userToken}){
    const [uname, setUname] = useState('');
    const [pass, setPass] = useState('');
    const [name, setName] = useState('');
    const [isChecked, setIsChecked] = useState(false);
    const [response, setResponse] = useState('')
    const [showResp, setShowResp] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault();
        ApiCreateUser()
    }

    function ApiCreateUser(){
        const hashedPass = bcrypt.hashSync(pass, '$2a$10$ovfJgA/SxVxsd3NeD3dMne'); //If u change the salt also change it in Login.js
        const genSalt = bcrypt.genSaltSync()
        const newToken = bcrypt.hashSync(genSalt);
        console.log(newToken)
        setShowResp(false);
        fetch(`http://localhost:8000/createuser?username=${uname}&password=${hashedPass}&fullname=${name}&newToken=${newToken}&adminPriv=${isChecked}&user=${user}&user_token=${userToken}`).then(res => res.json()).then(data => {
            if(!data.auth){
                setResponse('ERROR: Authentication Invalid!');
            }else if(!data.creation){
                setResponse(`The username ${uname} was already taken`);
            }else{
                setResponse(`The user ${uname} was created`);
            }
            setShowResp(true);
        });
    }

    return (
        <div>
            <div className="auth-form-container">
                <h2>Create User</h2>
            <form className="create-user-form" onSubmit={handleSubmit}>
                <label htmlFor="name">Full Name</label>
                <input value={name} onChange={(e) => setName(e.target.value)} type="name" placeholder="first and last name" id="name" name="name"  />
                <label htmlFor="uname">Username </label>
                <input value={uname} onChange={(e) => setUname(e.target.value)} type="username" placeholder="username" id="uname" name="uname" />
                <label htmlFor="password">Password</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                <lable className="checkbox-wrapper">Admin Privileges
                    <input className="cbChild" type="checkbox" checked={isChecked} onChange={() => setIsChecked((prev) => !prev)} />
                </lable>
                <button type="submit">Create</button>
            </form>
            </div>
            {showResp ? <h3>{response}</h3>: null}
        </div>
    )
}
