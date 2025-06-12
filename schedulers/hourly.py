import logging
from apscheduler.triggers.cron import CronTrigger
from findrum.interfaces import Scheduler
from datetime import datetime, date, time

logger = logging.getLogger("findrum")

class HourlyScheduler(Scheduler):
    def register(self, scheduler):
        hour = self.config.get("hour")
        minute = self.config.get("minute", 0)
        start_date_str = self.config.get("start_date")

        logger.info(f"🕒 Scheduler config → hour: {hour}, minute: {minute}, start_date: {start_date_str}")

        if start_date_str:
            try:
                start_date = datetime.fromisoformat(start_date_str)
            except Exception as e:
                logger.error(f"❌ Invalid start_date format: {start_date_str}")
                raise ValueError(f"Invalid start_date format: {start_date_str}") from e
        else:
            h = int(hour) if hour is not None else 0
            m = int(minute)
            start_date = datetime.combine(date.today(), time(hour=h, minute=m))

        logger.info(f"📅 Job will start at: {start_date.isoformat()}")

        trigger = CronTrigger(minute=minute, start_date=start_date)
        logger.info(f"🔁 CronTrigger created → minute: {minute}, start_date: {start_date}")

        scheduler.add_job(
            func=self._run_pipeline,
            trigger=trigger,
            id=self.pipeline_path,
            name=f"{self.pipeline_path} @ every hour at {minute:02d}m starting {start_date}",
            replace_existing=True
        )

        logger.info(f"✅ Job registered for pipeline: {self.pipeline_path}")