import React, { useState, useEffect } from "react";
import bcrypt from 'bcryptjs'
import './AuthForm.css';

export default function CreateUser({ user, userToken }) {
    const [uname, setUname] = useState('');
    const [pass, setPass] = useState('');
    const [name, setName] = useState('');
    const [isChecked, setIsChecked] = useState(false);
    const [response, setResponse] = useState('')
    const [showResp, setShowResp] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault();
        ApiCreateUser();
    }

    function ApiCreateUser() {
        if (pass.length > 72) {
            setResponse('Input exceeded limit')
            setShowResp(true);
        } else if (pass.length < 4) {
            setResponse('Password can be a minimum of 4 chars')
            setShowResp(true);
        } else {
            const hashedPass = bcrypt.hashSync(pass, '$2a$10$ovfJgA/SxVxsd3NeD3dMne'); //If u change the salt also change it in Login.js
            const genSalt = bcrypt.genSaltSync()
            const newToken = bcrypt.hashSync(genSalt);
            setShowResp(false);
            fetch(`http://localhost:8000/createuser?username=${uname}&password=${hashedPass}&fullname=${name}&newToken=${newToken}&adminPriv=${isChecked}&user=${user}&user_token=${userToken}`).then(res => res.json()).then(data => {
                setResponse(data.response);
                setShowResp(true);
                if (data.creation) {
                    setUname('');
                    setPass('');
                    setName('');
                    setIsChecked(false);
                }
            });
        }
    }

    useEffect(() => {
        window.scrollTo(0, 0)
    }, [])

    return (
        <div>
            <div className="auth-form-container">
                <h2>Create User</h2>
                <form className="create-user-form" onSubmit={handleSubmit}>
                    <label htmlFor="name">Full Name</label>
                    <input className="inputFields" value={name} onChange={(e) => setName(e.target.value)} type="name" placeholder="first and last name" id="name" name="name" />
                    <label htmlFor="uname">Username </label>
                    <input className="inputFields" value={uname} onChange={(e) => setUname(e.target.value)} type="username" placeholder="username" id="uname" name="uname" />
                    <label htmlFor="password">Password</label>
                    <input className="inputFields" value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                    <label className="checkbox-wrapper">
                        <input type="checkbox" checked={isChecked} onChange={() => setIsChecked((prev) => !prev)} />
                        <span >Admin Privileges</span>
                    </label>
                    <div className="AuthBtnContainer">
                        <button className="createBtn" type="submit">Create</button>
                    </div>
                </form>
            </div>
            {showResp ? <h3>{response}</h3> : null}
        </div>
    )
}
