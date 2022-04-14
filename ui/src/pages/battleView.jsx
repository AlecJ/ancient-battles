import React, { Component } from 'react';
import LeaderImages from '../components/leaderImages';
import HintsResultsAndControlsContainer from '../components/hintsResultsAndControlsContainer';
import { get_battle } from '../api/routes'

import styles from './styles/battleView.module.scss';
import './styles/defaultStyles.scss';


class BattleView extends Component {

  constructor(props) {
    super(props)

    this.state = {
      BattleIDList: [],
      currentBattle: null,
    }

    this.getBattle = this.getBattle.bind(this)
  }

  componentDidMount() {
    this.getBattle()
  }

  async getBattle() {
    const { BattleIDList } = this.state

    // if the user has a list of battles to go through, retrieve the next
    // battle by ID and remove it from the list
    if (BattleIDList.length > 0) {
      console.log(BattleIDList)
      const battleID = BattleIDList.shift()
      const data = await get_battle(battleID)
      this.setState({currentBattle: data.data.battle,
                     BattleIDList: BattleIDList})
    // if the user is just starting or has finished their list of battles
    // then they can get a new battle and a full list of battles
    } else {
      const data = await get_battle()
      console.log(data.data.list_of_battle_IDs)
      // remove first element from list of IDS
      data.data.list_of_battle_IDs.shift()
      this.setState({currentBattle: data.data.battle,
                     BattleIDList: data.data.list_of_battle_IDs})
    }
  }

    render() { 
        const { currentBattle } = this.state;
        console.log(currentBattle)

        return (
          !!currentBattle ?  
              <div className={styles.container}>
                
                <div className={styles.battleName}>
                  <h2>{currentBattle.battleName}</h2>
                </div>
        
                <LeaderImages currentBattle={currentBattle} />
        
                <HintsResultsAndControlsContainer getBattle={this.getBattle} currentBattle={currentBattle} />
                
              </div>
              :
                <div>LOADING</div>)
    }
}
 
export default BattleView;