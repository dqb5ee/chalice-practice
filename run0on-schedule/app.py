from chalice import Chalice
import boto3


app = Chalice(app_name='run0on-schedule')


instance_id=29428130032812

@app.schedule('cron(0 8 * * *)')
def daily_task():
    print("Turning on EC2 instance")
    ec2 = boto3.client('ec2')
    response = ec2.start_instances(instance_id)
