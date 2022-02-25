import React, { Component } from 'react';

import styles from './styles/results.module.scss';

class Results extends Component {
    state = { 
        wikipediaBlurb: 'The Battle of Alesia or Siege of Alesia (September 52 BC) was a military engagement in the Gallic Wars around the Gallic oppidum (fortified settlement) of Alesia in modern France, a major centre of the Mandubii tribe. It was fought by the Roman army of Julius Caesar against a confederation of Gallic tribes united under the leadership of Vercingetorix of the Arverni...',
        userHasGuessed: false,
        wikipediaLink: 'https://en.wikipedia.org/wiki/Battle_of_Alesia',
    }

    render() {
        const { wikipediaBlurb, wikipediaLink } = this.state;
        const { userHasGuessed } = this.props;

        return (
            <div className={styles.resultsContainer}>
                <div className={styles.result}>
                    {userHasGuessed ? <p>Correct!</p> : <p>Incorrect!</p>}
                </div>
                <div className={styles.wikipediaText}>
                    <p>{wikipediaBlurb}</p>
                </div>
                <div className={styles.wikipediaLink}>
                    <a href={wikipediaLink}>Read more on Wikipedia</a>
                </div>
                <div className={styles.nextMatchBtnContainer}>
                    <button className="btn">Next Match</button>
                </div>
            </div>
        );
    }
}
 
export default Results;