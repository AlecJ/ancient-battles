import React, { Component } from 'react';
import Controls from './controls';
import Hints from './hints';
import Results from './results';

import styles from './styles/hintsAndResultsContainer.module.scss';


class HintsResultsAndControlsContainer extends Component {
    state = { 
      guessed: false,
    }

    render() {
      const { guessed } = this.state

      return (
          <div className={styles.hintsAndResultsWindow}>
            <div className={`${styles.hintsAndResultsContainer} ${guessed ? styles.slideDown : styles.slideUp}`}>
              <Results />
              <Hints />
              <Controls />
            </div>
        </div>
      );
    }
}
 
export default HintsResultsAndControlsContainer;