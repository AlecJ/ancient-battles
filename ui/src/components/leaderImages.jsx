import React, { Component } from 'react';
import styles from './styles/leaderImages.module.scss';

export default (props) => {
    const { currentBattle } = props
    const { leaderAName, leaderBName, leaderAImageLink, leaderBImageLink } = currentBattle

    return (
        <React.Fragment>
            <div className={styles.icons}>
                <div id="leaderA" className={styles.leaderImageContainer}>
                    <img src={leaderAImageLink} />
                </div>
    
                <div id="leaderB" className={styles.leaderImageContainer}>
                    <img src={leaderBImageLink} />
                </div>
            </div>

            <div className={styles.leaderNames}>
                <div id="leaderAName">{leaderAName}</div>
                <div id="leaderBName">{leaderBName}</div>
            </div>
        </React.Fragment>
    );

}
