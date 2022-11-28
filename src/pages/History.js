import {useState, useEffect} from 'react'
import LoadingSpinner from '../components/LoadingSpinner'
import './History.css'

export default function History({user, userToken}) {
    const [isLoading, setLoading] = useState(false);
    const [historyDict, setHistoryDict] = useState('');
    const [error, setError] = useState('')

    useEffect(() => {
        setLoading(true)
        fetch(`http://localhost:8000/history?username=${user}&user_token=${userToken}`).then(res => res.json()).then(data => {
            setLoading(false)
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
            <div className="LoadingSpinner">
                {isLoading ? <LoadingSpinner></LoadingSpinner> : null}
            </div>
            <p>{historyDict}{error}</p>
        </div>
    )
}