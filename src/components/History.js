import {useState, useEffect} from 'react'
import './UserHistory.css'

export default function History({user}) {
    const [historyDict, setHistoryDict] = useState('');
    const [showHistory, setShowHistory] = useState(false);

    function ApiHistory(){
        fetch(`http://localhost:8000/history?username=${user}`).then(res => res.json()).then(data => {
            setHistoryDict(data)
        });
    }
    return(
        <div className='history'>
            <h1>HISTORY</h1>
            <button onClick={ApiHistory}>Show</button>
            <p>{historyDict.history}</p>
        </div>
    )
}