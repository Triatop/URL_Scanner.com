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
                console.log(data.history)
            }
        });
      }, [user,userToken]);

    return(
        <div className='history'>
            <h2>HISTORY</h2>
            <p>{error}</p>
            <div className="LoadingSpinner">
                {isLoading ? <LoadingSpinner></LoadingSpinner> : null}
            </div>
            <div className='histDict'>
                {Object.keys(historyDict).map((key, index) => {
                    return (
                    <div key={index}>
                        <p>URL: {historyDict[key].url}</p>
                        <p>DATE: {historyDict[key].date}</p>     
                        <p>SAFE: {historyDict[key].safe.toString()}</p>
                        <hr></hr>
                    </div>
                    );
                })}
            </div>
        </div>
    )
}