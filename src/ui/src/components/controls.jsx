import React, { Component } from 'react';

import styles from './styles/controls.module.scss'

class Controls extends Component {
    state = {  }


    render() {
        const { handleUserGuess } = this.props

        return (
            <div className={styles.controlsContainer}>
                  <button id="left-btn" className="btn" onClick={() => {handleUserGuess('A')}}>Left</button>
                  <button id="right-btn" className="btn" onClick={() => {handleUserGuess('B')}}>Right</button>
            </div> 
        );
    }
}
 
export default Controls;