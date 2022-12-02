import {useState, useEffect} from 'react'
import LoadingSpinner from '../components/LoadingSpinner'
import './History.css'
import CheckMark from '../components/CheckMark';
import CrossMark from '../components/CrossMark';

export default function History({user, userToken}) {
    const [isLoading, setLoading] = useState(false);
    const [historyDict, setHistoryDict] = useState('');
    const [error, setError] = useState('');
    const [showError, setShowError] = useState(false);
    const [showTop, setShowTop] = useState(false);

    useEffect(() => {
        setLoading(true)
        setShowError(false)
        setShowTop(false)
        fetch(`http://localhost:8000/history?username=${user}&user_token=${userToken}`).then(res => res.json()).then(data => {
            setLoading(false)
            if(!data.auth){
                setShowError(true)
                setError('ERROR: Authentication Invalid!')
            }else{
                setHistoryDict(data.history);
                setShowTop(true)
            }
        });
      }, [user,userToken]);

    return(
        <div className='history'>
            <h1>HISTORY</h1>
            { showTop ? 
            <ul className='columnNameContainer'>
                <li className='li1'>URL</li>
                <li className='li2'>DATE</li>
                <li className='li3'>SAFE</li>
            </ul>
            : null}
            {showError ? <p>{error}</p>: null}
            <div className="LoadingSpinner">
                {isLoading ? <LoadingSpinner></LoadingSpinner> : null}
            </div>
            <div>
                {Object.keys(historyDict).map((key, index) => {
                    return (
                            <div key={index}>
                                <ul className='histRow' id='history'>
                                    <li className='li1'>{historyDict[key].url}</li>
                                    <li className='li2'>{historyDict[key].date}</li>     
                                    <li className='li3'>{historyDict[key].safe ? <CheckMark showText={false}/>: <CrossMark showText={false}/>}</li>
                                </ul>
                            </div>
                    );
                })}
            </div>
        </div>
    )
}