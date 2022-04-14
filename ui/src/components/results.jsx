import React, { Component } from 'react';

import styles from './styles/results.module.scss';


export default (props) => {
    const { currentBattle, userIsCorrect, nextMatch } = props
    const { wikipediaBlurb, wikipediaLink } =  currentBattle

    return (
        <div className={styles.resultsContainer}>
            <div className={styles.result}>
                {userIsCorrect ? <p>Correct!</p> : <p>Incorrect!</p>}
            </div>
            <div className={styles.wikipediaText}>
                <p>{wikipediaBlurb}</p>
            </div>
            <div className={styles.wikipediaLink}>
                <a href={wikipediaLink}>Read more on Wikipedia</a>
            </div>
            <div className={styles.nextMatchBtnContainer}>
                <button className="btn" onClick={() => nextMatch()}>Next Match</button>
            </div>
        </div>
    );
}
