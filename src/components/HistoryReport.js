import '../pages/History'
import { useState } from 'react'
import CheckMark from '../components/CheckMark';
import CrossMark from '../components/CrossMark';

export default function ({ url, date, safe, report }) {
    const [arrow, setArrow] = useState('arrow down')
    const [showReport, setShowReport] = useState(false)

    const arrowClick = (event) => {
        event.preventDefault();
        setShowReport(!showReport)
        setArrow('arrow down' === arrow ? 'arrow up' : 'arrow down')
    };

    return (
        <div>
            <ul className='histRow' id='history'>
                <li className='li1'>{url}</li>
                <button className='arrowBtn' onClick={arrowClick}><i className={arrow}></i></button>
                <li className='li2'>{date}</li>
                <li className='li3'>{safe ? <CheckMark showText={false} /> : <CrossMark showText={false} />}</li>
            </ul>
            {showReport ? <section className="report"><div className='innerBorder'>{report}</div></section> : null}

        </div>
    )
}