import React, { Component } from 'react';

import styles from './styles/hints.module.scss';

class Hints extends Component {

    constructor(props) {
        super(props);

        this.state = { 
        }
    }



    render() { 
        const { currentBattle, revealHint, showDate, showLocation, showBelligerents } = this.props
        const { date, location, belligerentA, belligerentB } = currentBattle

        return (
            <div className={styles.hintsContainer}>
                <div className={styles.hints}>
                    <div id="Date">
                        <h2>Date</h2>
                        <div className={styles.reveal}
                             onClick={() => {revealHint('date')}}>
                            {showDate ? (
                                <p className={styles.fadeText}>{date}</p>
                            ) : (
                                <p>Click to reveal</p>
                            )}
                        </div>
                    </div>
                    <div id="Location">
                        <h2>Location</h2>
                        <div className={styles.reveal}
                             onClick={() => {revealHint('location')}}>
                            {showLocation ? (
                                <p className={styles.fadeText}>{location}</p>
                            ) : (
                                <p>Click to reveal</p>
                            )}
                        </div>
                    </div>
                    <div id="Belligerents">
                        <h2>Belligerents</h2>
                        <div className={styles.reveal}
                             onClick={() => {revealHint('belligerents')}}>
                            {showBelligerents ? (
                                <p className={styles.fadeText}>{belligerentA} | {belligerentB}</p>
                            ) : (
                                <p>Click to reveal</p>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
 
export default Hints;