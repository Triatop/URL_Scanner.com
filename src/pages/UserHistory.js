import {useState, useEffect} from 'react'
import LoadingSpinner from '../components/LoadingSpinner'
import './History.css'
import CheckMark from '../components/CheckMark';
import CrossMark from '../components/CrossMark';

export default function UserHistory({user, userToken}) {
    const [isLoading, setLoading] = useState(false);
    const [userHistoryDict, setUserHistoryDict] = useState('');
    const [error, setError] = useState('')

    useEffect(() => {
        setLoading(true);
        fetch(`http://localhost:8000/userhistory?username=${user}&user_token=${userToken}`).then(res => res.json()).then(data => {
            setLoading(false);    
            if(!data.auth){
                setError('ERROR: Authentication Invalid!')
            }else{
                setUserHistoryDict(data.userhistory);
            }
        });
      }, [user, userToken]);

    return(
        <div className='history'>
            <h1>HISTORY</h1>
            <div className="LoadingSpinner">
                {isLoading ? <LoadingSpinner></LoadingSpinner> : null}
            </div>
            <div>
                {Object.keys(userHistoryDict).map((key1, index1) => {
                    return (
                    <div key1={index1}>
                        <h2 className='keys'>{key1} </h2>
                        <ul className='columnNameContainer'>
                            <li className='li1'>URL</li>
                            <li className='li2'>DATE</li>
                            <li className='li3'>SAFE</li>
                        </ul>
                        {Object.keys(userHistoryDict[key1]).map((key2, index2) => {
                            return (
                            <div key2={index2}>
                                <ul className='histRow' id='history'>
                                    <li className='li1'>{userHistoryDict[key1][key2].url}</li>
                                    <li className='li2'>{userHistoryDict[key1][key2].date}</li>     
                                    <li className='li3'>{userHistoryDict[key1][key2].safe ? <CheckMark showText={false}/>: <CrossMark showText={false}/>}</li>
                                </ul>
                            </div>
                            );
                        })}
                        <hr/>
                    </div>
                    );
                })}   
            </div>
            <p>{error}</p>
        </div>
    )
}