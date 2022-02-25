import React, { Component } from 'react';

import styles from './styles/hints.module.scss';

class Hints extends Component {
    state = {
        showDate: true,
        showLocation: true,
        showBelligerents: true,
        date: 'September 52 BC',
        location: 'Alise-Sainte-Reine, France',
        belligerentA: 'Roman Republic',
        belligerentB: 'Gaulic Confederation',
    }

    render() { 
        const { showDate, showLocation, showBelligerents,
                date, location, belligerentA, belligerentB } = this.state

        return (
            <div className={styles.hintsContainer}>
                <div className={styles.hints}>
                    <div id="Date">
                        <h2>Date</h2>
                        <div className={styles.reveal}>
                            {showDate ? (
                                <p className={styles.fadeText}>{date}</p>
                            ) : (
                                <p>Click to reveal</p>
                            )}
                        </div>
                    </div>
                    <div id="Location">
                        <h2>Location</h2>
                        <div className={styles.reveal}>
                            {showLocation ? (
                                <p className={styles.fadeText}>{location}</p>
                            ) : (
                                <p>Click to reveal</p>
                            )}
                        </div>
                    </div>
                    <div id="Belligerents">
                        <h2>Belligerents</h2>
                        <div className={styles.reveal}>
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