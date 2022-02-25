import React, { Component } from 'react';
import Controls from './controls';
import Hints from './hints';
import Results from './results';

import styles from './styles/hintsAndResultsContainer.module.scss';


class HintsResultsAndControlsContainer extends Component {
    constructor(props) {
        super(props);

        this.state = { 
            userIsCorrect: null,
            answer: 'A',
        }
    }
    

    handleUserGuess = (guess) => {
        /*
        The user selects either LEFT or RIGHT to make their guess
        in the controls component. Once the user guesses, the result
        window is revealed and the user can move on to the next battle.
        */
        const { answer } = this.state;

        if (guess === answer) {
            this.setState({userIsCorrect: true})
        } else {
            this.setState({userIsCorrect: false})
        }
    }

    render() {
      const { userIsCorrect } = this.state

      console.log(userIsCorrect, !userIsCorrect, !!userIsCorrect);

      return (
          <div className={styles.hintsAndResultsWindow}>
            <div className={`${styles.hintsAndResultsContainer} ${userIsCorrect !== null ? styles.slideDown : styles.slideUp}`}>
              <Results userIsCorrect={userIsCorrect} />
              <Hints />
              <Controls handleUserGuess={this.handleUserGuess} />
            </div>
        </div>
      );
    }
}
 
export default HintsResultsAndControlsContainer;