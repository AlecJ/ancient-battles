import React, { Component } from 'react';
import Controls from './controls';
import Hints from './hints';
import Results from './results';

import styles from './styles/hintsAndResultsContainer.module.scss';


class HintsResultsAndControlsContainer extends Component {
    state = { 
      userHasGuessed: false,
    }

    handleUserGuess(guess) {
      /*
      The user selects either LEFT or RIGHT to make their guess
      in the controls component. Once the user guesses, the result
      window is revealed and the user can move on to the next battle.
      */
      // if (guess === 'A') {

      // } else if (guess === 'B') {
      //   continue
      // } else {
      //   // raise exception
      //   continue
      // }
      console.log('Click!')
      this.setState({userHasGuessed: true})
    }

    render() {
      const { userHasGuessed } = this.state

      return (
          <div className={styles.hintsAndResultsWindow}>
            <div className={`${styles.hintsAndResultsContainer} ${userHasGuessed ? styles.slideDown : styles.slideUp}`}>
              <Results userHasGuessed={userHasGuessed} />
              <Hints />
              <Controls handleUserGuess={this.handleUserGuess} />
            </div>
        </div>
      );
    }
}
 
export default HintsResultsAndControlsContainer;