import React, { Component } from 'react';

import styles from './styles/hints.module.scss';

class Hints extends Component {
    state = {  } 
    render() { 
        return (
            <div className={styles.hintsAndControlsContainer}>
                <div className={styles.hints}>
                  <div id="Date">
                    <h2>Date</h2>
                    {/* <div id="date-reveal" class="reveal" @click="revealDate">
                      <p v-if="showDate" class="fade_text">{{ date }}</p>
                      <p v-else>Click to reveal</p>
                    </div> */}
                  </div>
                  <div id="Location">
                    <h2>Location</h2>
                    {/* <div id="location-reveal" class="reveal" @click="revealLocation">
                      <p v-if="showLocation" class="fade_text">{{ location }}</p>
                      <p v-else>Click to reveal</p>
                    </div> */}
                  </div>
                  <div id="Belligerents">
                    <h2>Belligerents</h2>
                    {/* <div id="belligerents-reveal" class="reveal" @click="revealBelligerents">
                      <p v-if="showBelligerents" class="fade_text">{{ belligerentA }} | {{ belligerentB }}</p>
                      <p v-else>Click to reveal</p>
                    </div> */}
                    </div>
                  </div>
                </div>
        );
    }
}
 
export default Hints;