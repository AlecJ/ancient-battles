import React, { Component } from 'react';

import styles from './styles/hints.module.scss';

class Hints extends Component {
    state = {
        showDate: false,
        showLocation: false,
        showBelligerents: false,
        date: 'September 52 BC',
        location: 'Alise-Sainte-Reine, France',
        belligerentA: 'Roman Republic',
        belligerentB: 'Gaulic Confederation',
    }

    revealHint(hint) {
        if (hint === 'date') {
            this.setState({showDate: true});
        } else if (hint === 'location') {
            this.setState({showLocation: true});
        } else if (hint === 'belligerents') {
            this.setState({showBelligerents: true});
        } else {
            // error handling
        }
    }

    render() { 
        const { showDate, showLocation, showBelligerents,
                date, location, belligerentA, belligerentB } = this.state

        return (
            <div className={styles.hintsContainer}>
                <div className={styles.hints}>
                    <div id="Date">
                        <h2>Date</h2>
                        <div className={styles.reveal}
                             onClick={() => {this.revealHint('date')}}>
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
                             onClick={() => {this.revealHint('location')}}>
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
                             onClick={() => {this.revealHint('belligerents')}}>
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