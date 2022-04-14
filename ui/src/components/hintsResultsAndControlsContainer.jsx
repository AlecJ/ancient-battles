import React, { Component } from 'react';
import Controls from './controls';
import Hints from './hints';
import Results from './results';

import styles from './styles/hintsAndResultsContainer.module.scss';

const initialState  = {
    userIsCorrect: null,
    showDate: false,
    showLocation: false,
    showBelligerents: false,
}

class HintsResultsAndControlsContainer extends Component {

    constructor(props) {
        super(props);
        this.state = {...initialState }

        this.revealHint = this.revealHint.bind(this)
        this.nextMatch = this.nextMatch.bind(this)
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

    handleUserGuess = (guess) => {
        /*
        The user selects either LEFT or RIGHT to make their guess
        in the controls component. Once the user guesses, the result
        window is revealed and the user can move on to the next battle.
        */
        const { currentBattle } = this.props;
        const { answer } = currentBattle;

        if (guess === answer) {
            this.setState({userIsCorrect: true})
        } else {
            this.setState({userIsCorrect: false})
        }
    }

    nextMatch = () => {
        /*
        Once the user is finished with the result screen, they can press a
        "Next Match" button. This resets the user guess, and populates the first
        screen with data from a new battle.
        */
        const { getBattle } = this.props
        // get the next match
        getBattle()

        // reset state with new data
        this.setState({...initialState})
    }

    render() {
        const { currentBattle } = this.props
        const { userIsCorrect, showDate, showLocation, showBelligerents } = this.state

        return (
            <div className={styles.hintsAndResultsWindow}>
                <div className={`${styles.hintsAndResultsContainer} ${userIsCorrect !== null ? styles.slideDown : styles.slideUp}`}>
                <Results currentBattle={currentBattle} userIsCorrect={userIsCorrect} nextMatch={this.nextMatch} />
                <Hints currentBattle={currentBattle} revealHint={this.revealHint} showDate={showDate}
                        showLocation={showLocation} showBelligerents={showBelligerents} />
                <Controls handleUserGuess={this.handleUserGuess} />
                </div>
            </div>
        );
    }
}
 
export default HintsResultsAndControlsContainer;