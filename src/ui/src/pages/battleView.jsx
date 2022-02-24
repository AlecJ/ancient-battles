import React, { Component } from 'react';

import LeaderImages from '../components/leaderImages';
import HintsResultsAndControlsContainer from '../components/hintsResultsAndControlsContainer';

import styles from './styles/battleView.module.scss';


class BattleView extends Component {
    state = { 
        battleName: 'Battle of Alesia'
    }

    render() { 
        const { battleName } = this.state;

        return (
              <div className={styles.container}>
                
                <div className={styles.battleName}>
                  <h2>{ battleName }</h2>
                </div>
        
                <LeaderImages />
        
                <HintsResultsAndControlsContainer />
                
              </div>
          );
    }
}
 
export default BattleView;