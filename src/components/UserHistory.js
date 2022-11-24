import {useState, useEffect} from 'react'

export default function UserHistory({user}) {
    const [historyDict, setHistoryDict] = useState('');
    const [showHistory, setShowHistory] = useState(false);

    function ApiUserHistory(){
        fetch(`http://localhost:8000/userhistory?username=${user}`).then(res => res.json()).then(data => {
            setHistoryDict(data)
        });
    }
    return(
        <div className='history'>
            <h1>HISTORY</h1>
            <button onClick={ApiUserHistory}>Show</button>
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
        </div>
    )
}