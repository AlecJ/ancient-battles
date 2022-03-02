import React, { Component } from 'react';
import styles from './styles/leaderImages.module.scss';

class LeaderImages extends Component {
    state = { 
        leaderAName: 'Julius Casesar',
        leaderBName: 'Vercingetorix',
        leaderAImageLink: 'https://upload.wikimedia.org/wikipedia/commons/6/62/Retrato_de_Julio_C%C3%A9sar_%2826724093101%29_%28cropped%29.jpg',
        leaderBImageLink: 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Vercingetorix_stat%C3%A8re_MAN.jpg/800px-Vercingetorix_stat%C3%A8re_MAN.jpg',

        // .classPic.bard {
        //     background-image: url('/assets/dnd/bard.png');
        // }
    }

    render() {
        const { leaderAName , leaderBName, leaderAImageLink, leaderBImageLink } = this.state;

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
}

export default LeaderImages;