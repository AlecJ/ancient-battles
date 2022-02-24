import React, { Component } from 'react';

class HintsResultsAndControlsContainer extends Component {
    state = {  } 
    render() { 
        return (
            <div id="hints_and_result_window">
            {/* <div id="hints_and_result_container" :class="[guessed ? 'slideDown': 'slideUp']"> */}
  
              <div id="result_container">
                <div id="result" v-show="guessed">
                  <p v-if="guessed == result">Correct!</p>
                  <p v-else>Incorrect!</p>
                </div>
                <div id="wikipedia_text">
                  <p>{{ wikipediaBlurb }}</p>
                </div>
                <div id="wikipedia_link">
                  <a v-bind:href="wikipediaLink">Read more on Wikipedia</a>
                </div>
                <div id="next_match_button">
                  <button id="next-btn" class="btn">Next Match</button>
                </div>
              </div>
  
              <div id="hint_and_button_container">
                <div id="hints">
                  <div id="Date">
                    <h2>Date</h2>
                    <div id="date-reveal" class="reveal" @click="revealDate">
                      <p v-if="showDate" class="fade_text">{{ date }}</p>
                      <p v-else>Click to reveal</p>
                    </div>
                  </div>
                  <div id="Location">
                    <h2>Location</h2>
                    <div id="location-reveal" class="reveal" @click="revealLocation">
                      <p v-if="showLocation" class="fade_text">{{ location }}</p>
                      <p v-else>Click to reveal</p>
                    </div>
                  </div>
                  <div id="Belligerents">
                    <h2>Belligerents</h2>
                    <div id="belligerents-reveal" class="reveal" @click="revealBelligerents">
                      <p v-if="showBelligerents" class="fade_text">{{ belligerentA }} | {{ belligerentB }}</p>
                      <p v-else>Click to reveal</p>
                    </div>
                  </div>
                </div>
  
                <div id="buttons">
                  <button id="left-btn" class="btn" @click="guessLeft">Left</button>
                  <button id="right-btn" class="btn" @click="guessRight">Right</button>
                </div>
              </div>
            </div>
          </div>
        );
    }
}
 
export default HintsResultsAndControlsContainer;