import {useState, useEffect} from 'react'
import './History.css'

export default function UserHistory({user, userToken}) {
    const [historyDict, setHistoryDict] = useState('');
    const [error, setError] = useState('')

    useEffect(() => {
        fetch(`http://localhost:8000/userhistory?username=${user}&user_token=${userToken}`).then(res => res.json()).then(data => {
            if(!data.auth){
                setError('ERROR: Authentication Invalid!')
            }else{
                setHistoryDict(data.history);
            }
        });
      }, [user, userToken]);

    return(
        <div className='history'>
            <h1>HISTORY</h1>
            <div>
                {Object.keys(historyDict).map((key, index) => {
                    return (
                    <div key={index} className='keys'>
                        <h2>{key}: </h2>
                        <p>{historyDict[key]}</p>
                        <hr/>
                    </div>
                    );
                })}   
            </div>
            <p>{error}</p>
        </div>
    )
}