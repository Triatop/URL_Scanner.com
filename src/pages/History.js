import {useState, useEffect} from 'react'
import './History.css'

export default function History({user, userToken}) {
    const [historyDict, setHistoryDict] = useState('');
    const [error, setError] = useState('')

    useEffect(() => {
        fetch(`http://localhost:8000/history?username=${user}&user_token=${userToken}`).then(res => res.json()).then(data => {
            if(!data.auth){
                setError('ERROR: Authentication Invalid!')
            }else{
                setHistoryDict(data.history);
            }
        });
      }, [user,userToken]);

    return(
        <div className='history'>
            <h1>HISTORY</h1>
            <p>{historyDict}{error}</p>
        </div>
    )
}