import { Handler, APIGatewayEvent} from "aws-lambda";
import { IotData } from "aws-sdk";
import { invalid, success } from "./response";


export const iotMessageHandler: Handler  = async (
  event: APIGatewayEvent,
  _context,
  callback) => {  
      const endpoint = process.env.HOST;
      const encoding: Message = JSON.parse(event.body);
      const iotdata = new IotData({endpoint: endpoint});
      const params = {
          topic: encoding.topic,
          payload: JSON.stringify({message: encoding.message}),
          qos: 0
        };
      return iotdata.publish(params).promise().then(res => {
          const err = res.$response.error 
          return err ? callback(null, invalid(err)) : callback(null, success)
      }
  )
}