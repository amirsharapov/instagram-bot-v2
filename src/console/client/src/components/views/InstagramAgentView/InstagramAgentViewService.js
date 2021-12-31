import constants from "../../../utils/constants"
import socket from "../../../utils/sockets"

const {
  SOCKET_MESSAGE_TYPES: {
    START_PROGRAM
  }
} = constants;


export const startInstagramAgent = () => {
  const message = {
    type: START_PROGRAM,
    program: 'instagram_agent',
    task: 'research_hashtags',
    seed_hashtag: 'happyholidays'
  }

  const json = JSON.stringify(message)
  socket.send(json)
}