import * as restAPI from './base'

export const get_battle = async (id) => {
    try {
        const response = await restAPI.get(`/battle`, { battle_id: id })
        return response
    } catch (error) {
        return {}
    }
}