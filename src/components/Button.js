import './Button.css';
import {Link} from'react-router-dom';

const STYLES = ['btn--primary', 'btn--ooutline'];

const SIZES = ['btn--medium', 'btn--large'];

export const Button = ({children, type, onClick, buttonStyle, buttonSize}) => {
    const checButtonStyle = STYLES.includes(buttonStyle) ? buttonStyle : STYLES[0];
    const checButtonSize = SIZES.includes(buttonSize) ? buttonSize : SIZES[0]

    return(
        <Link to='/sing-up' className='btn-mobile'>
            <button 
                className={'btn ${checkButtonStyles} $checkButtonSize}'}
                onClick={onClick}
                type={type}
            >
                {children}
            </button>
        </Link>
    )
}